try:
    import scraper
    scraper.scrap_acadinfo()
    print("Success")
except Exception as e:
    print(str(e))
