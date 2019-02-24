

class TestHostApi(object):
    def test_all_hosts(self, mocked_api):
        mocked_api.all_hosts()
        mocked_api.session.get.assert_called_with(url=mocked_api._create_url('/hosts'), params={})

    def test_all_hosts_with_status(self, mocked_api):
        mocked_api.all_hosts(status='success')
        mocked_api.session.get.assert_called_with(url=mocked_api._create_url('/hosts'),
                                                  params={'status': 'success'})


class TestProjectApi(object):
    def test_all_projects(self, mocked_api):
        mocked_api.all_projects()
        expected_url = mocked_api._create_url('/projects')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)

    def test_project_by_id(self, mocked_api):
        mocked_api.project_by_id('project_id')
        expected_url = mocked_api._create_url('/projects/project_id')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)

    def test_recent_version_by_project(self, mocked_api):
        mocked_api.recent_version_by_project('project_id')
        expected_url = mocked_api._create_url('/projects/project_id/recent_versions')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)

    def test_patches_by_project(self, mocked_api):
        mocked_api.patches_by_project('project_id')
        expected_url = mocked_api._create_url('/projects/project_id/patches')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)

    def test_test_stats_by_project(self, mocked_api):
        mocked_api.test_stats_by_project('project_id')
        expected_url = mocked_api._create_url('/projects/project_id/test_stats')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)


class TestBuildApi(object):
    def test_build_by_id(self, mocked_api):
        mocked_api.build_by_id('build_id')
        expected_url = mocked_api._create_url('/builds/build_id')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)

    def test_tasks_by_build(self, mocked_api):
        mocked_api.tasks_by_build('build_id')
        expected_url = mocked_api._create_url('/builds/build_id/tasks')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)


class TestVersionApi(object):
    def test_version_by_id(self, mocked_api):
        mocked_api.version_by_id('version_id')
        expected_url = mocked_api._create_url('/versions/version_id')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)

    def test_builds_by_version(self, mocked_api):
        mocked_api.builds_by_version('version_id')
        expected_url = mocked_api._create_url('/versions/version_id/builds')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)


class TestPatchApi(object):
    def test_patch_by_id(self, mocked_api):
        mocked_api.patch_by_id('patch_id')
        expected_url = mocked_api._create_url('/patches/patch_id')
        mocked_api.session.get.assert_called_with(url=expected_url, params=None)