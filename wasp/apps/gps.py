import wasp

from micropython import const

FONT_SIZE = const(24)


class GPSApp():
	NAME = "GPS"

	def __init__(self):
		self.speed = ""
		self.distance = ""

	def foreground(self):
		wasp.watch.drawable.fill()
		self._draw()
		wasp.system.request_tick(1000)

	def tick(self, ticks):
		wasp.system.keep_awake()
		s = wasp.system.gps_info.get("speed", "0 km/h")
		d = wasp.system.gps_info.get("distance", "0 m")
		if self.speed != s or self.distance != d:
			self.speed = s
			self.distance = d
			self._draw()

	def _draw(self):
		draw = wasp.watch.drawable
		draw.string(self.speed, 0, 120-FONT_SIZE, width=240)
		draw.string(self.distance, 0, 120, width=240)

