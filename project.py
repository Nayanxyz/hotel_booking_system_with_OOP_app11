import pandas
from fpdf import FPDF


df = pandas.read_csv("project/articles.csv", dtype={"id":str})

class Articles:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.id, 'price'].squeeze()

    def available(self):
        in_stock = df.loc[df['id'] == self.id, 'in_stock'].squeeze()
        return in_stock

class Receipt:
    def __init__(self, article):
        self.article = article

    def pdf(self):
        from fpdf import FPDF

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt: {self.article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
book_id = input("write id for purchase: ")
articles = Articles(article_id=book_id)
if articles.available():
    receipt = Receipt(articles)
    receipt.pdf()
else:
    print("No article is there .")

