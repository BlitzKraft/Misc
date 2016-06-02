//Units are mm
$fn = 30;

minkowski() 
{
	difference()
	{
		hull()
		{
			cylinder(r = 10, h = 2, center = true, $fn = 4);
			translate([0,20,0]) cylinder(r = 10, h = 2, center = true, $fn = 4);
		}
		union()
		{
			rotate([0, 0, 45]) translate([10, 0, 0]) hull() 
			{ 
				translate([10, 0, 0]) cylinder(r = 1.5, h = 10, center = true);
				translate([-10, 0, 0]) cylinder(r = 1.5, h = 10, center = true);
			}
			translate([0, 20, 0]) rotate([0, 0, 45]) translate([-10, 0, 0]) hull() 
			{ 
				translate([10, 0, 0]) cylinder(r = 1.5, h = 10, center = true);
				translate([-10, 0, 0]) cylinder(r = 1.5, h = 10, center = true);
			}
		}
	}
	sphere(r = 0.4, $fn=12);
}
