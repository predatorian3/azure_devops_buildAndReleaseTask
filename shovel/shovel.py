"""Shovel Tasks File
"""


import os
from shovel import task


@task
def build():
  """Build the buildAndReleaseTask
  """
  os.chdir("tasks/buildAndReleaseTask")
  os.system("""npm install""")
  os.system("""npm run tsc""")


@task
def gen_uuid():
  """ Generate a UUID
  """
  import uuid
  print(uuid.uuid4())


@task
def package():
  """Package the Azure DevOps Extension
  """
  if os.name == 'nt':
    os.system('''.\\tasks\\buildAndReleaseTask\\node_modules\\.bin\\tfx extension create --manifest-globs vss-extension.json''')
  else:
    os.system('''./tasks/buildAndReleaseTask/node_modules/.bin/tfx extension create --manifest-globs vss-extension.json''')


@task
def publish():
  """Publish the Azure DevOps Extension
  """
  if os.name == 'nt':
    os.system('''.\\tasks\\buildAndReleaseTask\\node_modules\\.bin\\tfx extension publish --manifest-globs vss-extension.json --share-with myOrg''')
  else:
    os.system('''./tasks/buildAndReleaseTask/node_modules/.bin/tfs extension publish --manifest-globs vss-extension.json --share-with myOrg''')