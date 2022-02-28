import unittest
import repos_visual as rv

class ReposVisualTest(unittest.TestCase):
    ''' Test for repos_visual '''

    def setUp(self):
        ''' Call all the functions '''
        self.r = rv.get_response()
        self.repo_dicts = rv.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = rv.get_visual_data(
            self.repo_dicts)

    def test_get_response(self):
        ''' Test that we get a valid response '''
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        ''' Test that we're getting the data we think we are '''
        self.assertEqual(len(self.repo_dicts), 30)

        requir_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in requir_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main
