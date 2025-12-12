# Studio schema examples

This is a repository with examples of Seqera Studio schema definitions for various use cases.

The example in this main branch is a simple, minimal definition to use a pre-built image for a VS Code studio from a registry.

```
session:
    template:
        kind: "registry"
        registry: "public.cr.seqera.io/platform/data-studio-vscode:1.101.2-0.9"
```

You can find multiple other examples as the other branches of this repository.

### Available examples

* [example-env-var](https://github.com/seqeralabs/studio-schema-examples/tree/example-env-var) - A more extensive use of the schema that also configures dependencies and environment variables.
* [example-dockerfile](https://github.com/seqeralabs/studio-schema-examples/tree/example-dockerfile) - An example of how you can define a Dockerfile definition for a studio that will then be built and started as a studio in Seqera Platform.
* [example-cloning-disabled](https://github.com/seqeralabs/studio-schema-examples/tree/example-cloning-disabled) - By default, repositories used to configure a studio are then cloned inside the studio - this example shows how to disable that. 
* [example-barebones](https://github.com/seqeralabs/studio-schema-examples/tree/example-barebones) - A minimal, bare-bone definition of the schema that can be used as starting point and extended.

### Documentation

For more details on the Schema definition, see [latest official Seqera documentation](https://docs.seqera.io/platform-cloud/studios/add-studio-git-repo#create-the-required-configuration-files).