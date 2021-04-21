
def offer_link(link_number):
    x = []
    for point in range(1, link_number):
        mask = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(point)
        x.append(mask)
    return x



print(offer_link(9))