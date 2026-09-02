import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.camera = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)

    def start(self):
        while True:
            ret, frame = self.camera.read()

            if not ret:
                break

            cv2.imshow('Camera', frame)

            #Pressione a tecla 'q' para sair
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Libera a câmera e fecha as janelas
        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    camera = Camera()
    camera.start()