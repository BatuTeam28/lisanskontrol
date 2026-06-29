-- [[ BATU SCRIPT - MATRIX PREMIUM | FIXED RAYCAST + LOW FOV ]] --
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local Camera = workspace.CurrentCamera
local LocalPlayer = Players.LocalPlayer

-- 1. RAINBOW İMZA
local Signature = Drawing.new("Text")
Signature.Visible = true; Signature.Center = true; Signature.Outline = true
Signature.Font = 2; Signature.Size = 24
Signature.Position = Vector2.new(Camera.ViewportSize.X / 2, 30)
Signature.Text = "Matrix Premium Tg: @BatuX28 | Fixed Edition"

-- FOV ÇEMBERİ AYARI (Düşürüldü)
local FOVCircle = Drawing.new("Circle")
FOVCircle.Visible = true
FOVCircle.Radius = 70 -- FOV alanı daha küçük ve gizli hale getirildi
FOVCircle.Thickness = 1.5
FOVCircle.Filled = false
FOVCircle.Position = Vector2.new(Camera.ViewportSize.X / 2, Camera.ViewportSize.Y / 2)

-- 2. DÜŞMAN CHAMS & METİN ETİKETLERİ
local function AttachChams(p)
    if p == LocalPlayer then return end
    
    local H = Instance.new("Highlight")
    H.FillTransparency = 0.5
    H.OutlineTransparency = 0
    H.DepthMode = Enum.HighlightDepthMode.AlwaysOnTop
    
    local TextESP = Drawing.new("Text")
    TextESP.Visible = false
    TextESP.Center = true
    TextESP.Size = 14
    TextESP.Outline = true

    p.CharacterAdded:Connect(function(char)
        task.wait(0.2)
        H.Parent = char
    end)
    if p.Character then H.Parent = p.Character end

    RunService.RenderStepped:Connect(function()
        if p.Character and p.Character:FindFirstChild("HumanoidRootPart") and p.Character:FindFirstChild("Humanoid") and p.Team ~= LocalPlayer.Team and p.Character.Humanoid.Health > 0 then
            local col = Color3.fromHSV(tick() % 5 / 5, 1, 1)
            H.Enabled = true
            H.FillColor = col
            Signature.Color = col
            FOVCircle.Color = col
            
            local pos, on = Camera:WorldToViewportPoint(p.Character.HumanoidRootPart.Position)
            if on then
                TextESP.Visible = true
                TextESP.Position = Vector2.new(pos.X, pos.Y - 60)
                TextESP.Text = p.Name .. " [" .. math.floor(p.Character.Humanoid.Health) .. " HP]"
                TextESP.Color = col
            else
                TextESP.Visible = false
            end
        else
            H.Enabled = false
            TextESP.Visible = false
        end
    end)
end

for _, p in pairs(Players:GetPlayers()) do AttachChams(p) end
Players.PlayerAdded:Connect(AttachChams)

-- 3. GÜNCEL SAFE AIMBOT (Yeni Raycast Sistemi)
local function GetVisibleTarget()
    local bestTarget, dist = nil, math.huge
    local center = Vector2.new(Camera.ViewportSize.X / 2, Camera.ViewportSize.Y / 2)
    FOVCircle.Position = center
    
    for _, p in pairs(Players:GetPlayers()) do
        if p ~= LocalPlayer and p.Character and p.Character:FindFirstChild("Head") and p.Team ~= LocalPlayer.Team and p.Character.Humanoid.Health > 0 then
            local pos, on = Camera:WorldToViewportPoint(p.Character.Head.Position)
            if on then
                local screenPos = Vector2.new(pos.X, pos.Y)
                local fovDist = (screenPos - center).Magnitude
                
                -- Küçük FOV çemberinin kontrolü
                if fovDist <= FOVCircle.Radius then
                    -- Eski Ray yapısı yerine yeni RaycastParams yapısı kuruldu
                    local raycastParams = RaycastParams.new()
                    raycastParams.FilterType = Enum.RaycastFilterType.Exclude
                    raycastParams.FilterDescendantsInstances = {LocalPlayer.Character, Camera}
                    raycastParams.IgnoreWater = true
                    
                    local origin = Camera.CFrame.Position
                    local direction = (p.Character.Head.Position - origin).Unit * 1000
                    local raycastResult = workspace:Raycast(origin, direction, raycastParams)
                    
                    -- Engel kontrolü doğrulaması
                    if raycastResult and raycastResult.Instance:IsDescendantOf(p.Character) then
                        if fovDist < dist then 
                            bestTarget = p.Character.Head
                            dist = fovDist 
                        end
                    end
                end
            end
        end
    end
    return bestTarget
end

RunService.RenderStepped:Connect(function()
    local target = GetVisibleTarget()
    if target then
        -- Akıcı takip (Sarsıntısız eşitleme)
        Camera.CFrame = Camera.CFrame:Lerp(CFrame.new(Camera.CFrame.Position, target.Position), 0.15)
    end
end)
