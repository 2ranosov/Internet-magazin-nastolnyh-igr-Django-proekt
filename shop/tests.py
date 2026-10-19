from django.test import SimpleTestCase
from django.urls import reverse

class PageTests(SimpleTestCase):
    def test_pages_navigation_and_templates(self):
        for name in ('home', 'catalog', 'about'):
            with self.subTest(page=name):
                response = self.client.get(reverse('shop:' + name))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'shop/' + name + '.html')
                self.assertTemplateUsed(response, 'shop/base.html')
                self.assertTemplateUsed(response, 'shop/includes/header.html')
                self.assertTemplateUsed(response, 'shop/includes/footer.html')
                self.assertContains(response, '<header', count=1)
                self.assertContains(response, '<footer', count=1)
                self.assertContains(response, '/static/shop/css/styles.css', count=1)
                self.assertContains(response, '<header')
                self.assertContains(response, '<footer')
                self.assertContains(response, 'aria-current="page"', count=1)
                for target in ('home', 'catalog', 'about'):
                    self.assertContains(response, 'href="' + reverse('shop:' + target) + '"')

    def test_catalog_contains_all_six_games(self):
        response = self.client.get(reverse('shop:catalog'))
        self.assertContains(response, '<article class="game-card">', count=6)
        self.assertContains(response, 'Орбита')

    def test_unknown_page_returns_404(self):
        self.assertEqual(self.client.get('/missing-page/').status_code, 404)
