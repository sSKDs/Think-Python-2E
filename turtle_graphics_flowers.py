def arc(t, r, angle):
	arc_length = (2 * pi * r) * (angle / 360)
	n = int(arc_length / 9) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	t.lt(step_angle / 2)
	polyline(t, n, step_length, step_angle)
	t.rt(step_angle / 2)
    
def petal(t, r, angle):
	for i in range(2):
		arc(t, r, angle)
		t.lt(180 - angle)
        
def flower(t, r, n, angle):
	for i in range(n):
		petal(t, r, angle)
		t.lt(360.0 / n)
