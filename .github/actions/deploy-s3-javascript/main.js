const core = require('@actions/core');
const exec = require('@actions/exec');

async function run() {
    try {
        // Get input values
        const bucket = core.getInput('bucket', { required: true });
        const bucketRegion = core.getInput('bucket-region', { required: false });
        const distFolder = core.getInput('dist-folder', { required: true });

        // Upload files to S3
        const s3Uri = `s3://${bucket}`;
        core.info(`Uploading files from ${distFolder} to ${s3Uri} in region ${bucketRegion}...`);
        
        await exec.exec(`aws s3 sync ${distFolder} ${s3Uri} --region ${bucketRegion}`);

        core.notice('Successfully deployed to AWS S3!');
    } catch (error) {
        core.setFailed(`Deployment failed: ${error.message}`);
    }
}

run();
