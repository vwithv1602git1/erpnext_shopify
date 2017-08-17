from .shopify_requests import post_request,get_shopify_item_image
import datetime
def vwrite(contenttowrite):
    target = open("vtestlogfile.txt", 'a+')
    target.write("\n==========================="+str(datetime.datetime.now())+"===========================\n")
    target.write("\n"+str(contenttowrite)+"\n")
    target.close()

def getAllImages(shopify_product_id):
    testoutput = get_shopify_item_image(shopify_product_id)
    return testoutput

