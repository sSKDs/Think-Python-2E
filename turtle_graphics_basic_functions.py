def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def polygon(t, length, n):
	angle = 360 / n
	polyline(t, n, length, angle)
  
def arc(t, r, angle):
	arc_length = (2 * pi * r) * (angle / 360)
	n = int(arc_length / 9) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	t.lt(step_angle / 2)
	polyline(t, n, step_length, step_angle)
	t.rt(step_angle / 2)
    
def circle(t, r):
	arc(t, r, 360)
