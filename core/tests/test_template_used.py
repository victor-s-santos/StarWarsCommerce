import pytest

path_list_core_templates = [
    ('/', 'index.html'),
]

path_list_not_found_templates = [
    ('/doesnt-exist', '404.html'),
]

#index template
@pytest.mark.parametrize('link, template_name', path_list_core_templates)
def test_template_to_core_app(client, link, template_name):
    """Must return the corresponding page"""
    response = client.get(link) 
    assert template_name in (template.name for template in response.templates)

#404
@pytest.mark.parametrize('link, template_name', path_list_not_found_templates)
def test_not_found_template(client, link, template_name):
    """Must return the corresponding page"""
    response = client.get(link) 
    assert template_name in (template.name for template in response.templates)
