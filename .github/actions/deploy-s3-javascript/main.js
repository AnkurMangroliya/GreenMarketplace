const core = require('@actions/core')
const github = require('@actions/github')
const exec = require("@actions/exec")

function run() {
    //1) Get some inout values
    const bucket = core.getInput('bucket',{ required: true })
    const bucketRegion = core.getInput('bucket-region',{ required: true })
    const distFolder = core.getIDToken('dist-folder',{ require: true })
    
    //@2 upload file
    const s3Uri = `s3://${bucket}`
    exec.exec(`aws s3 sync ${distFolder} ${s3Uri}  --region @{buckerRegion}`)

    core.notice('Hello from the custom JavaScript Action! ')
}

run();