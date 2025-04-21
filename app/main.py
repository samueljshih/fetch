from fastapi import FastAPI, HTTPException
from app.models import Receipt
from app.logic import calculate_points
from app.store import save, retrieve

app = FastAPI(title="Receipt Processor", version="1.0.0")

@app.post("/receipts/process", status_code=200)
def process_receipt(receipt: Receipt):
    try:
        points = calculate_points(receipt)
        rid = save(receipt, points)
        return {"id": rid}
    except Exception:
        raise HTTPException(status_code=400, detail="The receipt is invalid. Please verify input.")

@app.get("/receipts/{rid}/points", status_code=200)
def get_points(rid: str):
    points = retrieve(rid)
    if points is None:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")
    return {"points": points}
