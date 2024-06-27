import uuid


def upload_product_image(instance, filename):
    return "{}/{}/{}".format("product_images", uuid.uuid4(), filename)
