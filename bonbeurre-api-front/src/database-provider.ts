import { DataSource } from 'typeorm';

export const databaseProviders = [
  {
    provide: 'DATA_SOURCE',
    useFactory: async () => {
      const dataSource = new DataSource({
        type: 'mysql',
        host: 'localhost',
        port: 30000,
        username: 'root',
        password: 'root',
        database: 'db_visu',    
        entities: [
          './entities/automate.entity.ts',
          './entities/donnee_mesuree.entity.ts',
          './entities/fichier.entity.ts',
          './entities/utilisateur.entity.ts',
          './entities/unite.entity.ts',
        ],
      
        synchronize: true,
      });

      return dataSource.initialize();
    },
  },
];