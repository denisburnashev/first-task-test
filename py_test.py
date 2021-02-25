from main import get_doc_owner_name, check_document_existance, add_new_doc, delete_doc


class TestFunction:

    def test_check_document_existance(self):
        assert check_document_existance('11-2') == True

    def test_get_doc_owner_name(self):
        assert get_doc_owner_name('10006') == 'Аристарх Павлов'

    def test_add_new_doc(self):
        assert add_new_doc('53242', 'passport', 'ALex', '3') == '3'

    def test_delete_doc(self):
        assert delete_doc('2207 876234') == '2207 876234'
