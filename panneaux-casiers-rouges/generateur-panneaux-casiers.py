#!/usr/bin python3
# -*- coding: utf-8 -*-

import sys


def generate_svg(nom, taille_mm):
	svg_template = """
<svg viewBox="0 0 {width}mm {height}mm" xmlns="http://www.w3.org/2000/svg">
  <style>
    text {{
      font: bold {size}mm Arial;
      alignment-baseline: middle;
      text-anchor: middle;
    }}
    rect {{
      fill: none;
      fill: none;
      stroke: red;
      stroke-width: 0.1mm;
      rx: 4mm;
    }}
    circle {{
      stroke: red;
      stroke-width: 0.1mm;
      fill: none;
    }}
  </style>
  <g>  
    <rect x="0" y="0" width="{width}mm" height="{height}mm"/>
    {holes}
    <text x="{x}mm" y="{y}mm">{nom}</text>
  </g>
  <g transform="translate({xeirlab_px} {yeirlab_px})">
    <g transform="matrix(0.03914788,0,0,0.03892303,-111.81729,21.06861)">
      <path d="m 3095.8,234.91 c -30.672,-3.1822 -51.462,-16.649 -63.42,-41.081 -8.85,-18.082 -12.218,-37.544 -11.022,-63.697 1.5981,-34.953 11.464,-75.087 28.976,-117.87 11.75,-28.71 31.361,-62.24 49.966,-85.43 16.781,-20.917 38.544,-40.551 54.065,-48.774 12.619,-6.686 49.38,-17.366 68.298,-19.842 8.4002,-1.0995 8.4769,-0.3546 1.4091,13.688 -13.968,27.752 -20.151,51.832 -20.151,78.471 0,31.092 5.9713,58.582 25.384,116.86 22.796,68.437 28.933,96.319 25.451,115.63 -4.5028,24.975 -20.778,35.504 -69.528,44.979 -33.538,6.5187 -68.259,9.2621 -89.427,7.066 z"/>
      <path d="m 2900.6,-142.24 c -15.507,-5.3586 -21.378,-12.625 -28.893,-35.76 -9.7653,-30.064 -15.058,-65.255 -15.192,-101.02 -0.1027,-27.402 1.0522,-34.764 7.6205,-48.576 5.1483,-10.826 17.567,-24.047 28.829,-30.693 15.492,-9.1418 36.807,-14.124 60.426,-14.124 71.447,0 168.41,39.55 224.42,91.536 22.246,20.648 32.246,33.723 39.449,51.579 9.3276,23.123 18.069,59.747 14.995,62.821 -1.4744,1.4744 -12.727,-2.3864 -25.211,-8.6502 -9.7392,-4.8864 -24.65,-9.9943 -38.574,-13.214 -13.897,-3.2136 -45.764,-4.5898 -57.79,-2.4956 -11.889,2.0704 -40.721,10.58 -86.555,25.546 -59.702,19.495 -84.568,25.446 -105.99,25.364 -7.132,-0.0271 -13.25,-0.83562 -17.541,-2.3184 z"/>
      <path d="m 3255.5,-168.86 c -0.3502,-0.56656 2.4068,-7.571 6.1266,-15.565 13.349,-28.689 18.993,-53.424 18.974,-83.151 -0.01,-17.99 -0.2792,-20.057 -4.7709,-36.827 -2.6173,-9.7722 -10.692,-35.789 -17.943,-57.815 -7.2513,-22.026 -15.449,-47.801 -18.216,-57.278 -23.84,-81.633 -12.358,-106.39 53.863,-116.13 29.435,-4.3311 94.203,-7.0948 107.49,-4.587 19.5,3.6794 41.464,21.466 50.565,40.948 7.3908,15.822 9.3638,26.924 9.3355,52.529 -0.054,48.542 -11.95,93.726 -38.805,147.4 -21.672,43.311 -53.539,85.252 -78.759,103.66 -12.672,9.2484 -36.291,18.987 -60.058,24.763 -12.504,3.039 -26.558,4.0809 -27.806,2.0614 z"/>
      <path d="m 3519.7,65.138 c -40.88,-3.2324 -86.929,-17.388 -135.32,-41.6 -35.555,-17.787 -65.158,-38.103 -87.224,-59.856 -18.714,-18.45 -25.338,-29.659 -34.164,-57.817 -4.2246,-13.477 -9.186,-33.731 -10.242,-41.811 l -0.8976,-6.8677 4.293,0.85859 c 2.3611,0.47222 10.88,3.7712 18.932,7.331 26.225,11.595 34.184,13.918 52.976,15.46 12.464,1.0231 22.788,1.0088 38.873,-0.0536 27.057,-1.7871 42.502,-5.5338 87.975,-21.34 48.332,-16.8 70.849,-23.655 91.305,-27.796 11.156,-2.2585 32.114,-2.6667 38.98,-0.75917 8.1822,2.2731 16.254,8.477 21.411,16.455 13.174,20.383 21.959,70.591 22.244,127.14 0.1261,24.977 -0.1059,28.095 -2.7074,36.366 -9.353,29.738 -38.977,49.54 -80.485,53.8 -12.506,1.2834 -15.272,1.3358 -25.945,0.49186 z"/>
    </g>
  </g>
</svg>
"""
	# -- Change me --
	horizontal_holes = 8
	vertical_holes = 6
	offset_mm = 5

	# -- Do not change me --
	DONT_EDIT_EXTERIOR_WIDTH_MM = 75
	DONT_EDIT_HOLE_DIAMETER_MM = 5.6
	DONT_EDIT_HOLE_SPACING_MM = (DONT_EDIT_EXTERIOR_WIDTH_MM - 8 * DONT_EDIT_HOLE_DIAMETER_MM) / 7
	total_width_mm = horizontal_holes * DONT_EDIT_HOLE_DIAMETER_MM + \
					(horizontal_holes - 1) * DONT_EDIT_HOLE_SPACING_MM +  2 * offset_mm
	total_height_mm = vertical_holes * DONT_EDIT_HOLE_DIAMETER_MM + \
					(vertical_holes - 1) * DONT_EDIT_HOLE_SPACING_MM +  2 * offset_mm
	hole_radius_mm = DONT_EDIT_HOLE_DIAMETER_MM / 2


	holes_template = """<circle cx="{x}mm" cy="{y}mm" r="{r}mm"/>\n"""
	holes = ""
	for i in range(horizontal_holes):
		for j in range(vertical_holes):
			x = i * (DONT_EDIT_HOLE_DIAMETER_MM + DONT_EDIT_HOLE_SPACING_MM) + hole_radius_mm + offset_mm
			y = j * (DONT_EDIT_HOLE_DIAMETER_MM + DONT_EDIT_HOLE_SPACING_MM) + hole_radius_mm + offset_mm
			# 4 corners in red
			if (i == 0 or i == horizontal_holes - 1) and (j == 0 or j == vertical_holes - 1):
				holes += holes_template.format(x=x, y=y, r=hole_radius_mm)
			else:
				pass
				# holes += holes_template.format(x=x, y=y, r=hole_radius_mm)
	
	xeirlab_px = (total_width_mm / 2 - 4) * 3.7795275591
	yeirlab_px = (offset_mm + 1 - 4) * 3.7795275591

	generated_svg = svg_template.format(width=total_width_mm, height=total_height_mm, size=taille_mm,
										xeirlab_px=xeirlab_px, yeirlab_px=yeirlab_px,
										holes=holes, x=total_width_mm / 2, y=total_height_mm / 2, nom=nom)

	with open(f"{nom}.svg", "w") as f:
		f.write(generated_svg)


if __name__ == "__main__":
	argv = sys.argv[1:]
	if len(argv) != 2:
		print(f"Usage: \033[93mpython3\033[0m {sys.argv[0]} \033[94m<nom>\033[0m \033[94m<police_mm>\033[0m")
		exit(1)
	nom = argv[0]
	if not nom.isalnum():
		raise ValueError("Le nom doit être alphanumérique")
	taille = argv[1]
	if not taille.isdigit():
		raise ValueError("La taille doit être un entier en millimètres")
	print(f"Génération de la plaque de \033[93m{nom}\033[0m avec une police de \033[93m{taille}mm\033[0m")
	generate_svg(nom, taille)
	print(f"\033[92mFichier généré !\033[0m ({nom}.svg)")
