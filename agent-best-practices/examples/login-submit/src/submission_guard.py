class SubmissionGuard:
    """Reject request IDs that were already accepted by this instance."""

    def __init__(self):
        self._accepted_request_ids = set()

    def accept(self, request_id):
        if not request_id:
            raise ValueError("request_id must not be empty")

        if request_id in self._accepted_request_ids:
            return False

        self._accepted_request_ids = {request_id}
        return True
