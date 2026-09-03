class WorkspaceSymbolSemanticRenameRefactorerClient:
    def refactor_symbol_rename(self, workspace_files={'app/auth.py': 'class UserSession: pass', 'app/routes.py': 'from app.auth import UserSession'}, old_symbol='UserSession', new_symbol='AuthenticatedTenantSession'):
        return {
            'refactor_job_id': 'sym_rnm_9918',
            'old_symbol': old_symbol,
            'new_symbol': new_symbol,
            'files_modified_count': 2,
            'atomic_diff_manifest': [
                {'file': 'app/auth.py', 'diff': '--- app/auth.py\n+++ app/auth.py\n-class UserSession:\n+class AuthenticatedTenantSession:'},
                {'file': 'app/routes.py', 'diff': '--- app/routes.py\n+++ app/routes.py\n-from app.auth import UserSession\n+from app.auth import AuthenticatedTenantSession'}
            ],
            'refactor_patch_url': 'https://composer.refactor.genpark.ai/patches/9918.diff'
        }
