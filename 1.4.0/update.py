import os

import audb
import audeer
import audformat


name = 'emodb'
previous_version = '1.3.0'
build_dir = './build'
build_dir = audeer.mkdir(build_dir)

db = audb.load_to(
    build_dir,
    name,
    version=previous_version,
    num_workers=8,
    only_metadata=True,
    cache_root=None,
    verbose=True,
)

# Download paper
rel_paper_path = 'extra/burkhardt2005.pdf'
abs_paper_path = audeer.path(build_dir, rel_paper_path)
audeer.mkdir(os.path.dirname(abs_paper_path))
audeer.download_url(db.meta['pdf'], abs_paper_path)

# Add paper as attachment
db.attachments['paper'] = audformat.Attachment(
    rel_paper_path,
    description='Interspeech paper about emodb.',
)

db.save(build_dir)
