'''
Questaão 25
Abrir uma imagem colorida, transformar para tom de cinza e aplique a técnica Crescimento de Regiões (Region Growing).
Para isto, faça no paint uma imagem 640×480 com alguns objetos em preto e o fundo seja branco.
Neste tópico irão existir mais de um objeto para segmentar, então existe mais de uma região.
Inicialize a semente com um clique em cada objeto, em que o primeiro clique rotule o objeto como região 1,
pintando a região encontrada de vermelho. Ao terminar de delimitar a região 2, clique em outro objeto, rotulando
esta região como 2 e pinte esta região de azul. Faça o mesmo para um terceiro objeto, pintando o mesmo de verde e
rotulando sua região como 3.
Obs: Ressalto que as regiões que não fazem parte de nenhum objeto devem possuir valor 0.
'''
import cv2
import numpy as np
from numba import njit


# Read a rgb image
image = cv2.imread('../input_images/objects.jpg')

# Transform to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a matrix that will contain the segmented region
segmented = np.zeros_like(grayscale_image)

seed = (0, 0)
event_count = 0


@njit
def region_growing(image, image_marked, seed=None):

    # Get the rows and columns of the image
    rows, cols = image.shape[:2]

    # Loop through the image until the region stop growing
    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                # Verify if we reach the ROI and search through the neighborhood to see if the pixel is of the same
                # object, then if the pixel is part of the object put them in the segmented image
                if image_marked[row, col] == 1:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 1
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 1
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 1
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 1
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 1
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 1
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 1
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 1
                        current_found += 1

                if image_marked[row, col] == 2:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 2
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 2
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 2
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 2
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 2
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 2
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 2
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 2
                        current_found += 1

                if image_marked[row, col] == 3:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 3
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 3
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 3
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 3
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 3
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 3
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 3
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 3
                        current_found += 1

    return image_marked


def mouse_event(event, x, y, flags, param):
    # Verify if the left button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        global event_count
        global segmented

        event_count += 1

        segmented[y, x] = event_count


if __name__ == '__main__':
    # Create a window, show the original image and wait for the click
    cv2.namedWindow('Mark object 1', 1)
    cv2.imshow('Mark object 1', grayscale_image)
    cv2.setMouseCallback('Mark object 1', mouse_event)

    cv2.waitKey(0)

    # Apply the region growing algorithm
    segmented_image = region_growing(grayscale_image, segmented)

    # Create a rgb image
    rows, cols = segmented_image.shape[:2]
    new_img = np.zeros([rows, cols, 3], np.uint8)

    # Paint the segmented region as the question describes
    new_img[np.where(segmented_image == 1)] = [0, 0, 255]
    new_img[np.where(segmented_image == 2)] = [255, 0, 0]
    new_img[np.where(segmented_image == 3)] = [0, 255, 0]


    # Show the result
    cv2.imshow('Segmented image', new_img)
    cv2.waitKey(0)