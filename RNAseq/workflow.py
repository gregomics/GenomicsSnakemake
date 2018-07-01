configfile: "config.yml"

SAMPLES = config["samples"].split()
OUTDIR  = config["outdir"]
INDIR  = config["indir"]
rule all: # this define the TARGET!! Watch out!
    input: expand(OUTDIR + "{sample}_cnt.tsv", sample = SAMPLES)

rule map_to_genome:
    input:
        INDIR + "{file}_R1.fq.gz"
    output: OUTDIR + "{file}.sam"
    params: genome = config["hisat2"]["genome"]
    threads: 4
    log:
        "logs/hisat2/{file}.log"
    shell: "(hisat2 -x {params.genome} -U {input}  -p {threads} > {output}) 2>&1 > {log}"

rule sam_to_bam:
    input: "{file}.sam"
    output: 
      temp("{file}.bam")
    params: threads = config["samtools"]["threads"]
    log: "logs/samtools/{file}.log"
    shell: "(samtools view -bS -@ {params.threads} {input} > {output}) > {log}"


rule sort_bam:
    input: "{file}.bam"
    output: 
      protected("{file}_sorted.bam")
    params: threads = config["samtools"]["threads"]
    log: "logs/samtools/{file}_sorting.log"
    message: "Executing sorting BAM  with {threads} threads on the following files {input}."
    shell: "(samtools view -bS -@ {params.threads} {input} > {output}) > {log}"

rule count_read_on_feature:
    input: "{file}_sorted.bam"
    output: "{file}_cnt.tsv"
    params: gtf     = config["readcount"]["gtf"], \
            strand  = config["readcount"]["strand"], \
            option = config["readcount"]["feat"], \
            summary = config["readcount"]["summary"], \
            phred   = config["readcount"]["phred"]
    threads: 4
    log: "logs/featureCount/{file}.log"
    message: "Executing sorting BAM  with {threads} threads on the following files {input}."
    shell: "(featureCounts -a {params.gtf} -o {output} -s {params.strand} -t {params.option} -g {params.summary} -Q {params.phred} {input}) 2>&1 > {log}"
