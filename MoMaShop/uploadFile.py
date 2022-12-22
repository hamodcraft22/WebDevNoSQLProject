def handle_uploaded_file(file, loc):
    with open('MoMaShop/static/MoMaShop/img/{0}/{1}'.format(loc,file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
