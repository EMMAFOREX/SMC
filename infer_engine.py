from ultralytics import YOLO
import cv2, os
from decision_logic import confidence_score
from journal import log_journal

model = YOLO("runs/detect/train/weights/best.pt")

def run_full_analysis(image_path):
    results = model(image_path)
    classes = results[0].boxes.cls.tolist()

    d = {
        "order_block": 0 in classes,
        "liquidity": 1 in classes,
        "fair_value_gap": 2 in classes,
        "stop_loss": 3 in classes,
        "take_profit": 4 in classes,
        "ob_fvg_alignment": True,
        "liquidity_sweep": True,
        "valid_stop_loss": True,
        "valid_take_profit": True,
        "h1_trend_match": True,
        "h4_trend_match": True
    }

    confidence = confidence_score(d)
    decision = "A+ SETUP" if confidence >= 80 else "REJECTED"

    output = None
    if decision == "A+ SETUP":
        annotated = results[0].plot()
        os.makedirs("outputs", exist_ok=True)
        output = os.path.join("outputs", os.path.basename(image_path))
        cv2.imwrite(output, annotated)

    log_journal({"image": image_path, "decision": decision, "confidence": confidence})
    return decision, confidence, output, "OK"
