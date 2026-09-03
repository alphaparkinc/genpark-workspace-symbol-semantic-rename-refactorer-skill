from client import WorkspaceSymbolSemanticRenameRefactorerClient

def main():
    client = WorkspaceSymbolSemanticRenameRefactorerClient()
    res = client.refactor_symbol_rename({}, 'TokenMgr', 'AuthTokenManager')
    print('Symbol Semantic Rename Refactorer: ' + res['refactor_job_id'] + ' (' + res['old_symbol'] + ' -> ' + res['new_symbol'] + ')')
    print('Files Modified: ' + str(res['files_modified_count']) + ' files')
    print('Patch URL: ' + res['refactor_patch_url'])

if __name__ == '__main__':
    main()
