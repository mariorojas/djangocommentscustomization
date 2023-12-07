from django_comments.abstracts import CommentAbstractModel


class ImprovedComment(CommentAbstractModel):
    class Meta(CommentAbstractModel.Meta):
        ordering = ['-submit_date',]
