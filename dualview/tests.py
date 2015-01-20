from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from dualview.views import home_page
from dualview.views import dual_view
from dualview.views import main_controls
from dualview.views import img_controls

# Create your tests here.
class PageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_root_url_resolves_to_dual_view(self):
        found=resolve('/dual_view/?ctrlImgId=7706&expImgId=7705')
        self.assertEqual(found.func, dual_view)
        
    def test_resolves_to_main_controls(self):
        found=resolve('/main_controls/')
        self.assertEqual(found.func, main_controls)
    
    def test_resolves_to_img_controls(self):
        found=resolve('/img_controls/')
        self.assertEqual(found.func, img_controls)
        
    
        
    

# Create your tests here.
