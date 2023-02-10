from __future__ import annotations
from typing import Tuple, Union
from tikzpy.drawing_objects.point import Point
from tikzpy.drawing_objects.drawing_object import DrawingObject


class Ellipse(DrawingObject):
    """
    A class to create ellipses in the tikz environment.

    Attributes :
        center (tuple) : Pair of floats representing the center of the ellipse
        x_axis (float): The length (in cm) of the horizontal axis of the ellipse
        y_axis (float): The length (in cm) of the vertical axis of the ellipse
    """

    def __init__(
        self,
        center: Union[Tuple[float, float], Point],
        x_axis: float,
        y_axis: float,
        options: str = "",
        action: str = "draw",
    ) -> None:
        self._center = Point(center)
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.options = options
        super().__init__(action, self.options)

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, new_center: Union[tuple, Point]) -> None:
        if isinstance(new_center, (tuple, Point)):
            self._center = Point(new_center)
        else:
            raise TypeError(f"Invalid type '{type(new_center)}' for center")

    @property
    def north(self):
        return self._center + (0, self.y_axis)

    @property
    def east(self):
        return self._center + (self.x_axis, 0)

    @property
    def south(self):
        return self._center - (0, self.y_axis)

    @property
    def west(self):
        return self._center - (self.x_axis, 0)

    @property
    def _command(self) -> str:
        return f"{self.center} ellipse ({self.x_axis}cm and {self.y_axis}cm)"

    def shift(self, xshift: float, yshift: float) -> None:
        self._center.shift(xshift, yshift)

    def scale(self, scale: float) -> None:
        self._center.scale(scale)
        self.x_axis *= scale
        self.y_axis *= scale

    def rotate(
        self, angle: float, about_pt: Tuple[float, float], radians: bool = False
    ) -> None:
        self._center.rotate(angle, about_pt, radians)
