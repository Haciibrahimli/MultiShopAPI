class Uploader:

    @staticmethod
    def upload_photo_partniors(instance, filename):
        return f"partniors/{filename}"

    @staticmethod
    def upload_photo_special_offer(instance, filename):
        return f"special_offer/{filename}"  

    def upload_photo_slider(instance, filename):
        return f" photo_slider/{filename}" 