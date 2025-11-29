{
  description = "Circuit Breaker Labs Python client development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        inherit (nixpkgs) lib;

        build = with pkgs; [
          uv
          openapi-python-client
        ];

        postProcessing = with pkgs; [
          ruff
          prettier
        ];
      in
      {
        devShells.default = pkgs.mkShell {
          LD_LIBRARY_PATH = lib.makeLibraryPath [ pkgs.stdenv.cc.cc ];

          buildInputs = with pkgs; [ mypy ] ++ build ++ postProcessing;
        };

        apps.generate =
          let
            generateScript = pkgs.writeShellApplication {
              name = "generate";
              runtimeInputs = build ++ postProcessing;
              text = ''
                echo "Using openapi-python-client version: $(openapi-python-client --version)"
                echo "Using config file at: $PWD/config.yaml"
                echo "Using additional templates from: $PWD/templates"

                openapi-python-client generate --url https://api.circuitbreakerlabs.ai/v1/openapi.json \
                  --output-path "$PWD" \
                  --overwrite \
                  --config "$PWD/config.yaml" \
                  --custom-template-path="$PWD/templates" \
                  --meta uv
              '';
            };
          in
          {
            type = "app";
            program = lib.getExe generateScript;
          };
      }
    );
}
