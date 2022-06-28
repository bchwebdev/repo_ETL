import { Module } from '@nestjs/common';
import { databaseProviders } from './database-provider';
import { StatsGraphiqueModule } from './stats-graphique/stats-graphique.module';


@Module({
  imports: [StatsGraphiqueModule],
  controllers: [],
  providers: [...databaseProviders],
})
export class AppModule {}
