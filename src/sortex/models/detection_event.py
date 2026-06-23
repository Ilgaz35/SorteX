from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Decision = Literal["accept", "reject", "unknown"]


@dataclass(frozen=True, slots=True)
class DetectionEvent:
    object_id: int
    frame_id: int
    timestamp_ms: float
    class_name: str
    decision: Decision
    confidence: float
    center_px: tuple[float, float]
    bbox_px: tuple[float, float, float, float]
