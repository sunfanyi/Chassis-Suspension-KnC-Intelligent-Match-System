# -*- mode: python -*-

block_cipher = None


a = Analysis(['appMain.py',
	'__init__.py',
	'D:\\Desktop\\match_system\\client_side\\__init__.py',
	'D:\\Desktop\\match_system\\client_side\\myFormCompare1.py',
	'D:\\Desktop\\match_system\\client_side\\myFormCompare2.py',
	'D:\\Desktop\\match_system\\client_side\\myFormImport.py',
	'D:\\Desktop\\match_system\\client_side\\myFormResult1.py',
	'D:\\Desktop\\match_system\\client_side\\myFormResult2.py',
	'D:\\Desktop\\match_system\\client_side\\myFormSetTarget.py',
	'D:\\Desktop\\match_system\\client_side\\myFormSetWeight1.py',
	'D:\\Desktop\\match_system\\client_side\\myFormSetWeight2.py',
	'D:\\Desktop\\match_system\\client_side\\myFormTargetItem.py',
	'D:\\Desktop\\match_system\\client_side\\myFormWelcome.py',
	'D:\\Desktop\\match_system\\client_side\\myMainWindow.py',
	'D:\\Desktop\\match_system\\client_side\\qss.py',
	'D:\\Desktop\\match_system\\client_side\\res_rc.py',
	'D:\\Desktop\\match_system\\client_side\\ui_MainWindow.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormCompare1.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormCompare2.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormImport.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormResult1.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormResult2.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormSetTarget.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormSetWeight1.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormSetWeight2.py',
	'D:\\Desktop\\match_system\\client_side\\ui_QWFormWelcome.py',
	'D:\\Desktop\\match_system\\database_establishment\\__init__.py',
	'D:\\Desktop\\match_system\\database_establishment\\curves_data.py',
	'D:\\Desktop\\match_system\\database_establishment\\data_extraction.py',
	'D:\\Desktop\\match_system\\database_establishment\\data_handling.py',
	'D:\\Desktop\\match_system\\database_establishment\\excel_formating.py',
	'D:\\Desktop\\match_system\\database_establishment\\get_files.py',
	'D:\\Desktop\\match_system\\database_establishment\\get_pdf_data_df.py',
	'D:\\Desktop\\match_system\\database_establishment\\get_test_data_df.py',
	'D:\\Desktop\\match_system\\database_establishment\\main_database.py',
	'D:\\Desktop\\match_system\\database_establishment\\vehicle_identity.py',
	'D:\\Desktop\\match_system\\similarity_evaluation\\__init__.py',
	'D:\\Desktop\\match_system\\similarity_evaluation\\detailed_similarity.py',
	'D:\\Desktop\\match_system\\similarity_evaluation\\get_curve_paths.py',
	'D:\\Desktop\\match_system\\similarity_evaluation\\main_similarity.py',
	'D:\\Desktop\\match_system\\similarity_evaluation\\overall_similarity.py',
	'D:\\Desktop\\match_system\\similarity_evaluation\\veh_key_data.py',
	'D:\\Desktop\\match_system\\similarity_evaluation\\veh_raw_data.py',
	'D:\\Desktop\\match_system\\similarity_evaluation\\weight_setting.py',
	'D:\\Desktop\\match_system\\target_evaluation\\__init__.py',
	'D:\\Desktop\\match_system\\target_evaluation\\detailed_reliability.py',
	'D:\\Desktop\\match_system\\target_evaluation\\main_target.py',
	'D:\\Desktop\\match_system\\target_evaluation\\overall_reliability.py',
	'D:\\Desktop\\match_system\\target_evaluation\\target_setting.py',
	'D:\\Desktop\\match_system\\target_evaluation\\veh_target_data.py',
	'D:\\Desktop\\match_system\\target_evaluation\\weight_setting2.py',
	'create_dir.py',
	'match_test_name.py'],
             pathex=['D:\\Desktop\\match_system'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='appMain',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='appMain')