

def test_main_blocks(app):
    index = 1
    app.log.info('Тест блока '+index+' в области "Распределение обязанностей"')
    app.open_test_page()
    graph = app.wd.find_elements_by_xpath('//section[@class="graphs"]/div')[index]  # убрать в модели
    info = app.wd.find_elements_by_xpath('//section[@class="info"]/div')[index]  # убрать в модели
    graph.find_element_by_xpath('a').click() #выделить
    assert str(graph.get_attribute('class')).endswith('graph-active'), app.log.error('Выбранный блок не активен')
    assert info.get_property('style').count('display'), app.log.error('Область подробного описание блока не отображается')
    req_list = info.find_elements_by_xpath('.//aside/ul/li')
    for req in req_list:
        name = req.find_element_by_tag_name('label').text
        assert req.find_element_by_tag_name('input').is_selected(), app.log.error('Чек бокс "'+name+'" не заполнен')
        req.find_element_by_tag_name('label').click()
        assert not req.find_element_by_tag_name('input').is_selected(), app.log.error('Чек бокс "'+name+'" остался заполнен')
        req.find_element_by_tag_name('label').click()
        assert req.find_element_by_tag_name('input').is_selected(), app.log.error('Чек бокс "'+name+'" не заполнен')
    app.log.info('Тест завершен, переходим к следующему')



    #app.wd.find_elements_by_xpath('//aside')[index].find_element_by_xpath('.//label[@for ="eye"]').click()
    #print(app.wd.find_elements_by_xpath('//aside')[index].find_element_by_id('eye').is_selected())
