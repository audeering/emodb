import audb2
import audfactory


audfactory.config.ARTIFACTORY_ROOT = 'https://audeering.jfrog.io/artifactory'
DB_ROOT = './build'


repository = audb2.Repository(
    name='data-public',
    host='https://audeering.jfrog.io/artifactory',
    backend='artifactory',
)
audb2.publish(
    DB_ROOT,
    version='1.1.0',
    repository=repository,
    num_workers=1,
    verbose=True,
)
