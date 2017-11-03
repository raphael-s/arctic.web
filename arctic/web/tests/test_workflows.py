from arctic.web.testing import ARCTIC_FUNCTIONAL
from ftw.lawgiver.tests.base import WorkflowTest


class TestARCTICWebWorkflowSpecification(WorkflowTest):
    layer = ARCTIC_FUNCTIONAL
    workflow_path = '../profiles/default/workflows/arctic_web_workflow'
