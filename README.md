# Studio schema examples

This is a repository with examples of Seqera Studio schema definitions for various use cases.

This branch showcases an example of how to disable cloning of the repository into the studio, so that it can be more easily shared and reused as a template.  

### Repository cloning inside studio

By default, when using a git repository when initializing a studio in Seqera Platform, upon studio launch the contents of git repository 
will be cloned inside the studio.  

However, you may not want that, for example, when you just want to have a shareable, reusable schema defining dependencies and environment variables (such as in this example).  
In that case you can disable the default cloning behaviour by setting.

```
session:
    clone:
        enabled: false
```

This will allow for the repository to be used purely as a easily shareable studio configuration managed on source control. 

Note: There are certain limitation and caveats to the cloning - refer to [official documentation for more details](For more details, see [latest official Seqera documentation](https://docs.seqera.io/platform-cloud/studios/add-studio-git-repo#create-the-required-configuration-files).

