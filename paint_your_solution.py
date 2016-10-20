# Skeleton code for participant solutions to the paint splash problem presented
# in workshop. To run the tests for this problem, run the paint_tests.py script

def paint_splash( pixels, click_point, target_color ):
    # Inputs:
    # pixels: [ [ int ] ]
    # click_point: ( int, int )
    # target_color: int
    x, y = click_point
    click_color = pixels[x][y]
    print('Starting! click point:', click_point, 'target color:', target_color)
    splash_recurse(pixels, click_point, click_color, target_color)

    return pixels



def splash_recurse(pixels, current_point, click_color, target_color, seen=None):
    if seen is None:
        seen = []
    x, y = current_point
    seen.append(current_point)
    print(current_point, 'click color:', click_color, 'target color:', target_color, 'seen:', seen)
    neighbors = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]

    index_filter = lambda t: t[0] >= 0 and t[1] >= 0 and t[0] < len(pixels) and t[1] < len(pixels[t[0]])
    color_filter = lambda t: pixels[t[0]][t[1]] == click_color
    seen_filter = lambda t: t not in seen

    filtered_neighbors = filter(seen_filter, filter(color_filter, filter(index_filter, neighbors)))

    print('filtered neighbors:', filtered_neighbors)
    try:
        current_point_color = pixels[x][y]
    except IndexError:
        return
    if current_point_color == click_color:
        print('setting', current_point, 'to target color')
        pixels[x][y] = target_color
        for coords in filtered_neighbors:
            print('recursing to:', coords)
            splash_recurse(pixels, coords, click_color, target_color, seen)
    else:
        print('return from the else!')




