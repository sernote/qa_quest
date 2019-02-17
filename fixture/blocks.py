

class Blockhelper:
    def __init__(self, app):
        self.app = app

    def graphs(self):
        wd = self.app.wd
        self.app.open_test_page()
        try:
            graphs = self.app.wd.find_elements_by_xpath('//section[@class="graphs"]/div')
        except self.app.exceptions.NoSuchElementException:
            self.app.log.critical('Столбцов с распределением времени нет на странице')
        else:
            return graphs

    def block_info(self):
        wd = self.app.wd
        self.app.open_test_page()
        try:
            block_info = self.app.wd.find_elements_by_xpath('//section[@class="info"]/div')
        except self.app.exceptions.NoSuchElementException:
            self.app.log.critical('Области с описанием блока нет на странице')
        else:
            return block_info

    def select_block_by_index(self, index):
        wd = self.app.wd
        link = self.graphs()[index].find_element_by_xpath('a')
        self.app.log.info('Переходим к блоку '+link.text)
        link.click()
