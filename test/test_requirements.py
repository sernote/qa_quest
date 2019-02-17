import pytest
num_blocks = list(range(4))


@pytest.mark.parametrize('index', num_blocks)
def test_requirements_blocks(app, index):
    graph = app.blocks.graphs()[index]
    app.log.info('Тест блока с индексом '+str(index)+' в области "Распределение обязанностей"')
    info = app.blocks.block_info()[index]
    app.blocks.select_block_by_index(index)
    assert str(graph.get_attribute('class')).endswith('graph-active'), app.log.error('Выбранный блок не активен')
    assert info.get_property('style').count('display'), app.log.error('Область описания блока не отображается')
    for req in app.blocks.req_list(index):
        name = req.find_element_by_tag_name('label').text
        assert req.find_element_by_tag_name('input').is_selected(), app.log.error('Чек бокс "'+name+'" не заполнен')
        req.find_element_by_tag_name('label').click()
        assert not req.find_element_by_tag_name('input').is_selected(), app.log.error('Чек бокс "'+name+'" остался заполнен')
        req.find_element_by_tag_name('label').click()
        assert req.find_element_by_tag_name('input').is_selected(), app.log.error('Чек бокс "'+name+'" не заполнен')
    app.log.info('Тест завершен, переходим к следующему')
