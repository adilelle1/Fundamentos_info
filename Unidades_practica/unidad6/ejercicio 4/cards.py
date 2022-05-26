class Card:

    def __init__(self, number, category, issue_date, expire_date, security_code):
        self.number = number
        self.category = category
        self.issue_date = issue_date
        self.expire_date = expire_date
        self.security_code = security_code

    def __str__(self) -> str:
        return f"\nNumero: {self.number}" \
               f"\nCategoria: {self.category}" \
               f"\nFecha de expiracion: {self.expire_date}" \
               f"\nCodigo de seguridad: {self.security_code}"

    def up_category(self, new_category):
        self.category = new_category


class DebitCard(Card):

    def __init__(self, number, category, issue_date, expire_date, security_code):
        super().__init__(number, category, issue_date, expire_date, security_code)


class CreditCard(Card):

    def __init__(self, number, category, issue_date, expire_date, security_code, purchase_limit):
        super().__init__(number, category, issue_date, expire_date, security_code)
        self.purhcase_limit = purchase_limit

    def __str__(self) -> str:
        return f"\nNumero: {self.number}" \
               f"\nCategoria: {self.category}" \
               f"\nFecha de expiracion: {self.expire_date}" \
               f"\nCodigo de seguridad: {self.security_code}" \
               f"\nLimite de compra: {self.purhcase_limit}"
