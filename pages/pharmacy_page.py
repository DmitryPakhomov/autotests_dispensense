class PharmacyPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self): pass
    def create_pharmacy(self, name): pass
    def open_pharmacy(self, name): pass
    def should_see_pharmacy(self, name): pass
    def edit_pharmacy(self, name): pass
    def open_integrations_tab(self): pass
    def add_integration(self, name): pass
    def should_see_integration(self, name): pass
    def open_ordering_tab(self): pass
    def add_supplier_integration(self, name): pass
    def remove_supplier_integration(self, name): pass
    def should_see_ordering_tab_empty(self): pass
