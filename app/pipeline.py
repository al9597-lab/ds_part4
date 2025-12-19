from sqlalchemy import text
from .db import get_session
from .model_inference import predict
from .config import MODEL_VERSION


def run_pipeline():
    session = get_session()

    try:
        # 1. Get documents that are NOT processed yet
        query = text("""
            SELECT doc_id, content
            FROM unstructured_document
            WHERE doc_id NOT IN (
                SELECT doc_id FROM document_inference
            );
        """)

        docs = session.execute(query).fetchall()

        if not docs:
            print("No new documents to process.")
            return

        print(f"Processing {len(docs)} documents...")

        # 2. For each doc → run model → insert results
        for doc_id, content in docs:
            label, score = predict(content)

            insert_query = text("""
                INSERT INTO document_inference
                (doc_id, predicted_disease, risk_score, model_version)
                VALUES (:doc_id, :label, :score, :version);
            """)

            session.execute(
                insert_query,
                {
                    "doc_id": doc_id,
                    "label": label,
                    "score": score,
                    "version": MODEL_VERSION
                }
            )

            print(f"Doc {doc_id} -> {label} ({score:.4f})")

        session.commit()
        print("Pipeline completed.")

    except Exception as e:
        session.rollback()
        print("Pipeline FAILED")
        print(e)

    finally:
        session.close()
