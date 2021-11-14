from django_ledger.models.items import ItemModelAbstract, ItemThroughModelAbstract
from django.db import models
from django_ledger.models.mixins import CreateUpdateMixIn  
from django_ledger.tests.base import DjangoLedgerBaseTest
from django.core.exceptions import ValidationError



class Test_Items(DjangoLedgerBaseTest):
    
    def test_avgCost(self):
        
        
        ItemModelAbstract.inventory_received_value = 14.0
        ItemModelAbstract.inventory_received = 7.0
        
        self.assertEqual(ItemModelAbstract.get_average_cost(ItemModelAbstract), 2.0)
        
        ItemModelAbstract.inventory_received = None
        self.assertEqual(ItemModelAbstract.get_average_cost(ItemModelAbstract), 0.0)
        
        
    def test_update_total_amount(self):
        
        ItemThroughModelAbstract.quantity = 3.0
        ItemThroughModelAbstract.unit_cost = 2.5
        ItemThroughModelAbstract.po_quantity = 2.0
        
        with self.assertRaises(ValidationError):
            ItemThroughModelAbstract.update_total_amount(ItemThroughModelAbstract)
            
            
    def test_clean(self):
    
        ItemModelAbstract.for_inventory = False
        ItemModelAbstract.is_product_or_service = False
        ItemModelAbstract.expense_account = None
        
        with self.assertRaises(ValidationError):
            ItemModelAbstract.clean(ItemModelAbstract)
            
        ItemModelAbstract.for_inventory = True
        ItemModelAbstract.is_product_or_service = True
        
        ItemModelAbstract.inventory_account = False
        ItemModelAbstract.cogs_account = False
        ItemModelAbstract.earnings_account = False
        
        with self.assertRaises(ValidationError):
            ItemModelAbstract.clean(ItemModelAbstract)
            
        ItemModelAbstract.for_inventory = True
        ItemModelAbstract.is_product_or_service = False
        
        ItemModelAbstract.inventory_account = False
        ItemModelAbstract.cogs_account = False
        
        with self.assertRaises(ValidationError):
            ItemModelAbstract.clean(ItemModelAbstract)
            
        ItemModelAbstract.for_inventory = False
        ItemModelAbstract.is_product_or_service = True
        
        ItemModelAbstract.earnings_account = False
        
        with self.assertRaises(ValidationError):
            ItemModelAbstract.clean(ItemModelAbstract)
            
        
        
        
        
        
        