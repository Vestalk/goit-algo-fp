
import argparse
import math

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def draw_pythagoras_tree(ax, x, y, size, angle, level, max_level, branch_angle=45):
    if level > max_level:
        return

    rad = math.radians(angle)
    dx, dy = size * math.cos(rad), size * math.sin(rad)
    px, py = -dy, dx

    p0 = (x, y)
    p1 = (x + dx, y + dy)
    p2 = (x + dx + px, y + dy + py)
    p3 = (x + px, y + py)

    # колір від коричневого (стовбур) до зеленого (листя)
    t = level / max(max_level, 1)
    color = (0.45 * (1 - t), 0.25 + 0.5 * t, 0.1 * (1 - t))
    ax.add_patch(Polygon([p0, p1, p2, p3], closed=True, facecolor=color, edgecolor="black", linewidth=0.3))

    a = math.radians(branch_angle)
    left_size = size * math.cos(a)
    right_size = size * math.sin(a)

    draw_pythagoras_tree(ax, *p3, left_size, angle + branch_angle, level + 1, max_level, branch_angle)
    apex_x = p3[0] + left_size * math.cos(rad + a)
    apex_y = p3[1] + left_size * math.sin(rad + a)
    draw_pythagoras_tree(ax, apex_x, apex_y, right_size, angle + branch_angle - 90, level + 1, max_level, branch_angle)


def main():
    parser = argparse.ArgumentParser(description="Дерево Піфагора")
    parser.add_argument("level", nargs="?", type=int, help="рівень рекурсії (напр. 8)")
    args = parser.parse_args()

    level = args.level
    while level is None or level < 0:
        try:
            level = int(input("Введіть рівень рекурсії (0-15): "))
        except ValueError:
            print("Потрібне ціле невід'ємне число.")
            level = None
    if level > 15:
        print("Рівень обмежено до 15 (інакше малювання буде дуже повільним).")
        level = 15

    fig, ax = plt.subplots(figsize=(9, 7))
    draw_pythagoras_tree(ax, -0.5, 0, 1, 0, 0, level)
    ax.set_aspect("equal")
    ax.autoscale_view()
    ax.axis("off")
    ax.set_title(f"Дерево Піфагора, рівень рекурсії = {level}")
    plt.show()


if __name__ == "__main__":
    main()
