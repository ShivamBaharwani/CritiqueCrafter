searchString = request.form['content'].replace(" ","")
flipkart_url = "https://www.flipkart.com/search?q=" + searchString
uClient = uReq(flipkart_url)
flipkartPage = uClient.read()
uClient.close()
flipkart_html = bs(flipkartPage, "html.parser")
            # bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            # del bigboxes[0:3]
bigboxes = flipkart_html.findAll("div", {"class": "tUxRFH"})
# if len(bigboxes) == 0:
#     logging.info("No products found for this search.")
#     return "No products found"