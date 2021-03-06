dtn_map = {'amx': {'/GPFS/CENTRAL': '/xf17id1'},
            'bmm': None,
            'chx': {'/XF11ID': '/xf11id1-central',
                    '/XF11ID/data': '/xf11id1-central/data',
                    '/nsls2/xf11id': '/xf11id1-central',
                    '/nsls2/xf11id1': '/xf11id1-central',
                    '/nsls2/xf11id1/data': '/xf11id1-central/data'},
            'cms': {'/nsls2/xf11bm': '/xf11bm',
                    '/GPFS/xf11bm': '/xf11bm'},
            'csx': {'/GPFS/xf23id/xf23id1': '/xf23id1/xf23id1',
                    '/GPFS/xf23id/xf23id2': '/xf23id1/xf23id2'},
            'esm': {'/GPFS/xf23id':	'/nsls2/xf23id1',
                    '/direct/XF21ID1': '/xf23id1'},
            'fmx': {'/GPFS/CENTRAL': '/xf17id2'},
            'fxi': {'/NSLS2/xf18id1/DATA': '/xf18id1/data',
                    '/NSLS2/xf18id1/DATA/Andor': '/xf18id1/data/Andor',
                    '/NSLS2/xf18id1/DATA/detA1': '/xf18id1/data/detA1'},
            'ios': {'/GPFS/xf23id/xf23id1': '/xf23id1/xf23id1',
                    '/GPFS/xf23id/xf23id2': '/xf23id1/xf23id2'},
            'isr': {'/GPFS/xf04id': '/xf04id1'}, #/GPFS/xf04id -> /nsls2/xf04id1
            'iss': {'/GPFS/xf08id/': '/xf08id', #/GPFS/xf08id -> /nsls2/xf08id
                    '/nsls2/xf08id': '/xf08id',
                    '/nsls2/xf08id/data': '/xf08id/data'},
            'ixs': None,
            'jpls': None,
            'lix': {'/GPFS/CENTRAL/XF16ID1/test/': None,
                    '/GPFS/xf16id': '/xf16id1',                     #/GPFS/xf16id -> /nsls2/xf16id1
                    '/GPFS/xf16ide/exp_path/': '/xf16id1/exp_path',
                    '/tmp/': None},
            'pdf': {'/SHARE/img': None,
                    '/nsls2/xf28id1': '/xf28id1',
                    '/nsls2/xf28id1/data': '/xf28id1/data',
                    '/nsls2/xf28id1/data/dex_data': '/xf28id1/data/dex_data',
                    '/nsls2/xf28id1/data/pe1_data': '/xf28id1/data/pe1_data',
                    '/tmp': None},
            'qas': {'/nsls2/xf07bm' : '/xf07bm'},
            'rsoxs': {'/DATA/images': None,
                      '/DATA/images/data': None,
                      '/mnt/zdrive': None},
            'six': {'/XF02ID1': None,           # /XF02ID1 -> /direct/XF02ID1 which is empty.
                    '/nsls2/xf02id1': '/xf02id1'},
            'smi': {'/GPFS/': None,
                    '/GPFS/xf12id1/data/MAXS/images': '/xf12id2/MAXS/images',
                    '/data': '/xf12id2/data' },
            'srx': {'/XF05IDD': '/xf05id1-central/XF05ID1', # Guess
                    '/data': '/xf05id1-central/data', # Guess
                    '/epicsdata': None,
                    '/nsls2/xf05id1': '/xf05id1-central',
                    '/nsls2/xf05id1/XF05ID1': '/xf05id1-central/XF05ID1',
                    '/nsls2/xf05id1/XF05ID1/dexela': '/xf05id1-central/XF05ID1/dexela',
                    '/tmp': None},
            'tes': {'/nsls2/xf08bm/XF08BM': '/xf08bm/data', # Bad guess
                    '/nsls2/xf08bm/data': '/xf08bm/data'},
            'xfm': {'/mnt/xspress3/data-srv2': None, # Path has no data anymore.
                    '/nsls2/xf04bm/data': '/xf04bm/data',
                    '/tmp/pe_img': None},
            'xfp': None,
            'xpd': {'/XF28IDC/XF28ID1': '/xf28id2/',
                    '/XF28IDC/XF28ID1/pe1_data/GeRM': '/xf28id2/pe1_data/GeRM',
                    '/direct/XF28ID1': None,
                    '/direct/XF28ID2': None,
                    '/nsls2/xf28id2': '/xf28id2',
                    '/tmp': None},
            'xpdd': {'/data/bf_data': '/xf28id2/bf_data',
                     '/epics': None,
                     '/mnt/ws3': None,
                     '/mnt/ws4': None,
                     '/mnt/ws4/XPDD_Data1': None,
                     '/nsls2': '',
                     '/nsls2/xf28id2' : '/xf28id2',
                     '/nsls2/xf28id2/bf_data': '/xf28id2/bf_data',
                     '/nsls2/xf28id2/dex_data': '/xf28id2/dex_data',
                     '/tmp/xpdsim_m2zab6q': None,
                     'F:\\dex_data': None,
                     'F:\\dex_data\\': None,
                     'Z:\\dex_data': None,
                     '\\nsls2\\xf28id2\\dex_data': None}}


root_map = {'amx': {'/GPFS/CENTRAL': '/nsls2/amx/data/9b93d7bd6cae59a0df7e56ef417774f7'},
 'chx': {'/XF11ID': '/nsls2/chx/data/c2a51221a864383a51807e006f5aad3a',
  '/XF11ID/data': '/nsls2/chx/data/f5d4e7f429a0b19644ba8bd21a6592da',
  '/nsls2/xf11id': '/nsls2/chx/data/b84fab57af84185bb8e251a348dd7174',
  '/nsls2/xf11id1': '/nsls2/chx/data/693d922c286afa25a73ef622d3ff3b6c',
  '/nsls2/xf11id1/data': '/nsls2/chx/data/6e4c0ff61ef00a76c87d8ea905de0fc5'},
 'cms': {'/nsls2/xf11bm': '/nsls2/cms/data/1b3786e7381a7bfbe04cb680cafc73aa',
  '/GPFS/xf11bm': '/nsls2/cms/data/53cd4d82617fe71f674a246c08e39d06'},
 'csx': {'/GPFS/xf23id/xf23id1': '/nsls2/csx/data/ae6e79261202c4239d2d4afdabc1b62e',
  '/GPFS/xf23id/xf23id2': '/nsls2/csx/data/9abcc999dad4362a17e46fc50d960f2c'},
 'esm': {'/GPFS/xf23id': '/nsls2/esm/data/fd4f109d5b80f7a4ca080e59f86247a0',
  '/direct/XF21ID1': '/nsls2/esm/data/cfb8ace7052a01700c3e6190324f1262'},
 'fmx': {'/GPFS/CENTRAL': '/nsls2/fmx/data/9b93d7bd6cae59a0df7e56ef417774f7'},
 'fxi': {'/NSLS2/xf18id1/DATA': '/nsls2/fxi/data/b1bd8e057dfd11901daae6933c7f00d7',
  '/NSLS2/xf18id1/DATA/Andor': '/nsls2/fxi/data/f1fdee311b9ea3f07adfc97e23010b41',
  '/NSLS2/xf18id1/DATA/detA1': '/nsls2/fxi/data/79d8766ba7e33c543015c986206783b4'},
 'ios': {'/GPFS/xf23id/xf23id1': '/nsls2/ios/data/ae6e79261202c4239d2d4afdabc1b62e',
  '/GPFS/xf23id/xf23id2': '/nsls2/ios/data/9abcc999dad4362a17e46fc50d960f2c'},
 'isr': {'/GPFS/xf04id': '/nsls2/isr/data/8b4349189d7296ce34842a20415372ad'},
 'iss': {'/GPFS/xf08id/': '/nsls2/iss/data/437733c36e583c21f2e199d37c248d16',
  '/nsls2/xf08id': '/nsls2/iss/data/ad5d08ffffe436b6c9b6d9246414be3d',
  '/nsls2/xf08id/data': '/nsls2/iss/data/550c12d9b12093f85a00913367b5e6b8'},
 'lix': {'/GPFS/xf16id': '/nsls2/lix/data/bcac0ed4f0d8d5bcf7e6393c6e0c415a',
  '/GPFS/xf16ide/exp_path/': '/nsls2/lix/data/c7ca66a3145ff2dbea8f51f63293a056'},
 'pdf': {'/nsls2/xf28id1': '/nsls2/pdf/data/289e51509c0a51ef24ee47d7db90db69',
  '/nsls2/xf28id1/data': '/nsls2/pdf/data/25dc112e14771a643049571112dbc8d1',
  '/nsls2/xf28id1/data/dex_data': '/nsls2/pdf/data/ef61bc0c4ec3b04793517e7ce622b8cd',
  '/nsls2/xf28id1/data/pe1_data': '/nsls2/pdf/data/f3727154ffcaa2885d9543fb11f6f541'},
 'qas': {'/nsls2/xf07bm': '/nsls2/qas/data/ba769df4b007fc819dc271d270bcb99d'},
 'rsoxs': {},
 'six': {'/nsls2/xf02id1': '/nsls2/six/data/49a55b3a14efcb23e543260d39522d13'},
 'smi': {'/GPFS/xf12id1/data/MAXS/images': '/nsls2/smi/data/354c7ff530e124a00da029071eddd644',
  '/data': '/nsls2/smi/data/4caa791091d21d23e63637080226f370'},
 'srx': {'/XF05IDD': '/nsls2/srx/data/a3a8e12b2aa682b91db66a5b973db4e9',
  '/data': '/nsls2/srx/data/4caa791091d21d23e63637080226f370',
  '/nsls2/xf05id1': '/nsls2/srx/data/4424e1ed75ee4e5e6dd0713967c00bb7',
  '/nsls2/xf05id1/XF05ID1': '/nsls2/srx/data/a04d8f634c51eff3f3a114d6ee033d46',
  '/nsls2/xf05id1/XF05ID1/dexela': '/nsls2/srx/data/467257172ebfacf4e5236de96c73c975'},
 'tes': {'/nsls2/xf08bm/XF08BM': '/nsls2/tes/data/1eb1b44734b1367fbeadfbb282c670a1',
  '/nsls2/xf08bm/data': '/nsls2/tes/data/8827f271de086af57ceba0af6fbc55dc'},
 'xfm': {'/nsls2/xf04bm/data': '/nsls2/xfm/data/d83d879ae5fdd3480ec3b3a2de9fc4f2'},
 'xpd': {'/XF28IDC/XF28ID1': '/nsls2/xpd/data/2dae78d275c5ac0343285a659fd57ec2',
  '/XF28IDC/XF28ID1/pe1_data/GeRM': '/nsls2/xpd/data/3595d8ed279016ff0d94e96a4e336261',
  '/nsls2/xf28id2': '/nsls2/xpd/data/b6d46e31e7ede1257a3d0e0a76dd2b5d'},
 'xpdd': {'/data/bf_data': '/nsls2/xpdd/data/ada2ba3e58c7b9ec2256426a6220acf4',
  '/nsls2': '/nsls2/xpdd/data/cf045c28b7535837b47aa07015c224c7',
  '/nsls2/xf28id2': '/nsls2/xpdd/data/b6d46e31e7ede1257a3d0e0a76dd2b5d',
  '/nsls2/xf28id2/bf_data': '/nsls2/xpdd/data/fabad61fcbabdbcb245d410f64522f47',
  '/nsls2/xf28id2/dex_data': '/nsls2/xpdd/data/12b9fbbbd620a7755189c2e4f7c0d668'}}


endpoint_map = {'amx': {'/xf17id1': '/nsls2/amx/data/9b93d7bd6cae59a0df7e56ef417774f7'},
                'chx': {'/xf11id1-central': '/nsls2/chx/data/693d922c286afa25a73ef622d3ff3b6c',
                        '/xf11id1-central/data': '/nsls2/chx/data/6e4c0ff61ef00a76c87d8ea905de0fc5'},
                'cms': {'/xf11bm': '/nsls2/cms/data/53cd4d82617fe71f674a246c08e39d06'},
                'csx': {'/xf23id1/xf23id1': '/nsls2/csx/data/ae6e79261202c4239d2d4afdabc1b62e',
                        '/xf23id1/xf23id2': '/nsls2/csx/data/9abcc999dad4362a17e46fc50d960f2c'},
                'esm': {'/nsls2/xf23id1': '/nsls2/esm/data/fd4f109d5b80f7a4ca080e59f86247a0',
                        '/xf23id1': '/nsls2/esm/data/cfb8ace7052a01700c3e6190324f1262'},
                'fmx': {'/xf17id2': '/nsls2/fmx/data/9b93d7bd6cae59a0df7e56ef417774f7'},
                'fxi': {'/xf18id1/data': '/nsls2/fxi/data/b1bd8e057dfd11901daae6933c7f00d7',
                        '/xf18id1/data/Andor': '/nsls2/fxi/data/f1fdee311b9ea3f07adfc97e23010b41',
                        '/xf18id1/data/detA1': '/nsls2/fxi/data/79d8766ba7e33c543015c986206783b4'},
                'ios': {'/xf23id1/xf23id1': '/nsls2/ios/data/ae6e79261202c4239d2d4afdabc1b62e',
                        '/xf23id1/xf23id2': '/nsls2/ios/data/9abcc999dad4362a17e46fc50d960f2c'},
                'isr': {'/xf04id1': '/nsls2/isr/data/8b4349189d7296ce34842a20415372ad'},
                'iss': {'/xf08id': '/nsls2/iss/data/ad5d08ffffe436b6c9b6d9246414be3d',
                        '/xf08id/data': '/nsls2/iss/data/550c12d9b12093f85a00913367b5e6b8'},
                'lix': {'/xf16id1': '/nsls2/lix/data/bcac0ed4f0d8d5bcf7e6393c6e0c415a',
                        '/xf16id1/exp_path': '/nsls2/lix/data/c7ca66a3145ff2dbea8f51f63293a056'},
                'pdf': {'/xf28id1': '/nsls2/pdf/data/289e51509c0a51ef24ee47d7db90db69',
                        '/xf28id1/data': '/nsls2/pdf/data/25dc112e14771a643049571112dbc8d1',
                        '/xf28id1/data/dex_data': '/nsls2/pdf/data/ef61bc0c4ec3b04793517e7ce622b8cd',
                        '/xf28id1/data/pe1_data': '/nsls2/pdf/data/f3727154ffcaa2885d9543fb11f6f541'},
                'qas': {'/xf07bm': '/nsls2/qas/data/ba769df4b007fc819dc271d270bcb99d'},
                'rsoxs': {},
                'six': {'/xf02id1': '/nsls2/six/data/49a55b3a14efcb23e543260d39522d13'},
                'smi': {'/xf12id2/MAXS/images': '/nsls2/smi/data/354c7ff530e124a00da029071eddd644',
                        '/xf12id2/data': '/nsls2/smi/data/4caa791091d21d23e63637080226f370'},
                'srx': {'/xf05id1-central/XF05ID1': '/nsls2/srx/data/a04d8f634c51eff3f3a114d6ee033d46',
                        '/xf05id1-central/data': '/nsls2/srx/data/4caa791091d21d23e63637080226f370',
                        '/xf05id1-central': '/nsls2/srx/data/4424e1ed75ee4e5e6dd0713967c00bb7',
                        '/xf05id1-central/XF05ID1/dexela': '/nsls2/srx/data/467257172ebfacf4e5236de96c73c975'},
                'tes': {'/xf08bm/data': '/nsls2/tes/data/8827f271de086af57ceba0af6fbc55dc'},
                'xfm': {'/xf04bm/data': '/nsls2/xfm/data/d83d879ae5fdd3480ec3b3a2de9fc4f2'},
                'xpd': {'/xf28id2/': '/nsls2/xpd/data/2dae78d275c5ac0343285a659fd57ec2',
                        '/xf28id2/pe1_data/GeRM': '/nsls2/xpd/data/3595d8ed279016ff0d94e96a4e336261',
                        '/xf28id2': '/nsls2/xpd/data/b6d46e31e7ede1257a3d0e0a76dd2b5d'},
                'xpdd': {'/xf28id2/bf_data': '/nsls2/xpdd/data/fabad61fcbabdbcb245d410f64522f47',
                         '': '/nsls2/xpdd/data/cf045c28b7535837b47aa07015c224c7',
                         '/xf28id2': '/nsls2/xpdd/data/b6d46e31e7ede1257a3d0e0a76dd2b5d',
                         '/xf28id2/dex_data': '/nsls2/xpdd/data/12b9fbbbd620a7755189c2e4f7c0d668'}}

roots = {'amx': ['', '/tmp', '/tmp/'],
 'bmm': ['/home/xspress3'],
 'chx': ['',
  '/XF11ID',
  '/XF11ID/data',
  '/nsls2/xf11id',
  '/nsls2/xf11id1',
  '/nsls2/xf11id1/data'],
 'cms': ['', '/', '/GPFS/xf11bm', '/nsls2/xf11bm'],
 'csx': ['', '/GPFS/xf23id/xf23id1', '/GPFS/xf23id/xf23id2'],
 'esm': ['', '/direct/XF21ID1'],
 'fmx': [''],
 'fxi': ['/',
  '/NSLS2/xf18id1/DATA',
  '/NSLS2/xf18id1/DATA/Andor',
  '/NSLS2/xf18id1/DATA/detA1',
  '/dev/shm'],
 'ios': ['', '/GPFS/xf23id/xf23id1', '/GPFS/xf23id/xf23id2'],
 'isr': ['/GPFS/xf04id'],
 'iss': ['', '/', '/GPFS/xf08id/', '/nsls2/xf08id', '/nsls2/xf08id/data'],
 'ixs': [],
 'jpls': ['/nsls2/jpls/data'],
 'lix': ['',
  '/',
  '/GPFS/CENTRAL/XF16ID1/test/',
  '/GPFS/xf16id',
  '/GPFS/xf16id/exp_path/',
  '/tmp/'],
 'pdf': ['/SHARE/img',
  '/nsls2/xf28id1',
  '/nsls2/xf28id1/data',
  '/nsls2/xf28id1/data/dex_data',
  '/nsls2/xf28id1/data/pe1_data',
  '/tmp'],
 'qas': ['/epics/',
  '/home/softioc/',
  '/home/softioc/tmp/',
  '/home/xf07bm/',
  '/nsls2/data/xf07bm/pb_data/',
  '/nsls2/xf07bm',
  '/nsls2/xf07bm/data',
  '/nsls2/xf07bm/data/pb_data',
  '/nsls2/xf07bm/data/pb_data/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/07/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/07/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/27/',
  '/nsls2/xf0bm/data/pb_data',
  '/nsls2/xf0bm/data/pizza_box_data/2018/03/08/'],
 'rsoxs': ['/DATA/images', '/DATA/images/data', '/mnt/zdrive'],
 'six': ['/XF02ID1', '/nsls2/xf02id1'],
 'smi': ['/', '/GPFS', '/GPFS/xf12id1/data/MAXS/images', '/data'],
 'srx': ['',
  '/',
  '/XF05IDD',
  '/data',
  '/epicsdata',
  '/nsls2/xf05id1',
  '/nsls2/xf05id1/XF05ID1',
  '/nsls2/xf05id1/XF05ID1/dexela',
  '/tmp'],
 'tes': ['/nsls2/xf08bm/XF08BM', '/nsls2/xf08bm/data'],
 'xfm': ['/mnt/xspress3/data-srv2', '/nsls2/xf04bm/data', '/tmp/pe_img'],
 'xfp': [],
 'xpd': ['',
  '/',
  '/XF28IDC/XF28ID1',
  '/XF28IDC/XF28ID1/pe1_data/GeRM',
  '/direct/XF28ID1',
  '/direct/XF28ID2',
  '/nsls2/xf28id2',
  '/tmp'],
 'xpdd': ['/',
  '/data/bf_data',
  '/epics',
  '/mnt/ws3',
  '/mnt/ws4',
  '/mnt/ws4/XPDD_Data1',
  '/nsls2',
  '/nsls2/xf28id2',
  '/nsls2/xf28id2/bf_data',
  '/nsls2/xf28id2/dex_data',
  '/tmp/xpdsim_m2zab6q',
  'F:\\dex_data',
  'F:\\dex_data\\',
  'Z:\\dex_data',
  '\\nsls2\\xf28id2\\dex_data']}
